import { Component, inject } from '@angular/core';
import { Message, MessageQueues, MessageService } from '../services/message.service';
import { MarkdownComponent } from "ngx-markdown";
import { HttpClient } from '@angular/common/http';
import { marked } from 'marked';
import { gfmHeadingId } from "marked-gfm-heading-id";

@Component({
  selector: 'app-content',
  imports: [MarkdownComponent],
  templateUrl: './content.html',
  styleUrl: './content.scss'
})
export class Content {

  private http = inject(HttpClient);
  data = ""
  sidebarVisible: boolean = true;
  columnCount: number = 1;
  columnNumbers = [1];
  activeRenderer = 1;
  pages: Map<number, string> = new Map([
    [1, ''],
    [2, ''],
    [3, ''],
    [4, '']
  ]);
  pageData: Map<number, string> = new Map([
    [1, ''],
    [2, ''],
    [3, ''],
    [4, '']
  ]);

  constructor(private messageService: MessageService) {
    marked.use(gfmHeadingId());
    this.messageService.subscribeToQueue(MessageQueues.SIDEBAR).subscribe((message) => {
      this.sidebarVisible = (message.getPayload() as any).visible;
    });
    this.messageService.subscribeToQueue(MessageQueues.COLUMN_SELECTOR).subscribe((message) => {
      this.columnCount = (message.getPayload() as any).columns;
      this.columnNumbers = Array.from({ length: this.columnCount }, (_, i) => i + 1);
      console.log(this.pages)
    });
    this.messageService.subscribeToQueue(MessageQueues.DOCUMENT_SELECTOR).subscribe((message) => {
      console.log(message);
      this.pages.set(this.activeRenderer, '/wiki' + (message.getPayload() as any).path);
      console.log(this.pages)
      this.fetch_data(this.pages.get(this.activeRenderer));
    });
  }

  fetch_data(path: string | undefined) {
    console.log(path)
    if (!path) {
      return;
    }
    this.http.get(path, {responseType: 'text'}).subscribe((response) => {
      const parsed = marked(response)
      if (typeof parsed === 'string') {
        this.pageData.set(this.activeRenderer, parsed);
        this.chooseActiveRenderer();
      } else if (parsed instanceof Promise) {
        parsed.then((result: string) => {
          this.pageData.set(this.activeRenderer, result);
          this.chooseActiveRenderer();
        });
      }
    })
  }

  chooseActiveRenderer() {
    if (this.columnCount > this.activeRenderer) {
      this.activeRenderer += 1;
    }
  }

  onLoad(event: string) {
    // your code here
  }
  onError(event: string | Error) {

  }
  onClick(event: PointerEvent) {
    let href = ((event.target as HTMLElement)?.getAttribute('href') ?? '');
    if (!href) {
      href = ((event.target as HTMLElement)?.parentElement?.getAttribute('href') ?? '');
    }
    if (href.startsWith('#')) {
      return;
    }
    event.preventDefault();
    const target = event.target as HTMLElement;
    let path = target.getAttribute('href');
    if (path) {
      this.messageService.sendMessage(new Message(MessageQueues.DOCUMENT_SELECTOR, {path: path}));
    }
  }
}

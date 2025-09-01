import { Component } from '@angular/core';
import { MarkdownComponent } from 'ngx-markdown';

// Import ColumnSelector from its correct path
import { ColumnSelector } from '../column-selector/column-selector';
import { Message, MessageQueues, MessageService } from '../services/message.service';
@Component({
  selector: 'app-sidebar',
  imports: [MarkdownComponent, ColumnSelector],
  templateUrl: './sidebar.html',
  styleUrl: './sidebar.scss'
})
export class Sidebar {

  sidebarVisible: boolean = true;

  constructor(private messageService: MessageService) {
    this.messageService.subscribeToQueue(MessageQueues.SIDEBAR).subscribe((message) => {
      this.sidebarVisible = (message.getPayload() as any).visible;
    });
  }

  // Add the onLoad method to handle the load event
  onLoad(event: any): void {
    // You can add your logic here, for now just log the event
  }

  onError(event: any): void {
  }

  onClick(event: Event): void {
    if (((event.target as HTMLElement)?.className ?? '') == 'deadlink') {
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

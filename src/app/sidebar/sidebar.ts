import { Component } from '@angular/core';
import { MarkdownService, MarkdownComponent } from 'ngx-markdown';

@Component({
  selector: 'app-sidebar',
  imports: [MarkdownComponent],
  templateUrl: './sidebar.html',
  styleUrl: './sidebar.scss'
})
export class Sidebar {
  constructor(public markdownService: MarkdownService) { }


  // Add the onLoad method to handle the load event
  onLoad(event: any): void {
    // You can add your logic here, for now just log the event
  }

  onError(event: any): void {
    console.error('Error loading markdown:', event);
  }
}

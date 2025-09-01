import { Component } from '@angular/core';
import { MessageService } from '../services/message.service';
import { Message, MessageQueues } from '../services/message.service';

@Component({
  selector: 'app-header',
  imports: [],
  templateUrl: './header.html',
  styleUrl: './header.scss'
})
export class Header {
  sidebar_visible: boolean = true;
  constructor(private messageService: MessageService) {}

  toggleSidebar() {
    this.sidebar_visible = !this.sidebar_visible;
    this.messageService.sendMessage(new Message(MessageQueues.SIDEBAR, { visible: this.sidebar_visible }));
  }
}

import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { MessageService } from '../services/message.service';
import { Message, MessageQueues } from '../services/message.service';

@Component({
  selector: 'app-column-selector',
  imports: [CommonModule, FormsModule],
  templateUrl: './column-selector.html',
  styleUrl: './column-selector.scss'
})
export class ColumnSelector {
  columnOptions = [
    { value: 1, label: '1 Column' },
    { value: 2, label: '2 Columns' },
    { value: 3, label: '3 Columns' },
    { value: 4, label: '4 Columns' },
  ];

  selectedValue: number = 1;

  constructor(private messageService: MessageService) {}

  isSelected(value: number): boolean {
    return this.selectedValue === value;
  }

  onCheckboxChange(value: number): void {
    this.selectedValue = value;
    this.messageService.sendMessage(new Message(MessageQueues.COLUMN_SELECTOR, { columns: this.selectedValue }));
  }
}

import { Component, OnInit, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Sidebar } from "./sidebar/sidebar";
import { Header } from "./header/header";
import { Content } from "./content/content";

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, Sidebar, Header, Content],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App implements OnInit {
  protected readonly title = signal('markdown-renderer');
  isSidebarCollapsed = false;

  ngOnInit(): void {

  }

  toggleSidebar() {
    console.log('called');
    this.isSidebarCollapsed = !this.isSidebarCollapsed;
  }
}

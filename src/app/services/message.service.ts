import { Injectable } from "@angular/core";
import { Subject } from "rxjs";
import { filter } from "rxjs/operators";

@Injectable({ providedIn: 'root'})
export class MessageService{
    private subject = new Subject<Message>();

    sendMessage(message: Message) {
        this.subject.next(message);
    }

    getMessage() {
        return this.subject.asObservable();
    }

    subscribeToQueue(queueName:string) {
      return this.subject.asObservable().pipe(
        filter((message) => message.getQueue() == queueName)
      );
    }
}

export class MessageQueues {
    public static SIDEBAR = 'sidebar'
    public static COLUMN_SELECTOR = 'columnSelector'
    public static DOCUMENT_SELECTOR = 'documentSelector'
}

export class Message {
    private queue: string;
    private payload: object;

    constructor(queue: string, payload: object) {
        this.queue = queue;
        this.payload = payload;
    }

    getQueue() {
        return this.queue;
    }

    getPayload() {
        return this.payload;
    }

    setQueue(queue: string) {
        this.queue = queue;
    }

    setPayload(payload: object) {
        this.payload = payload;
    }
}

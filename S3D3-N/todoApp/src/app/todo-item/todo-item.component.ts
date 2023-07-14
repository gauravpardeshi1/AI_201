import { Component,Input  } from '@angular/core';
import { Todo } from '../todo';
import { TodoService } from '../todos';
@Component({
  selector: 'app-todo-item',
  templateUrl: './todo-item.component.html',
  styleUrls: ['./todo-item.component.css']
})
export class TodoItemComponent {
  @Input() todo: Todo = { id: 0, title: '', description: '', completed: false };
  
  constructor(private todoService: TodoService) {}
  
  markAsCompleted(): void {

    this.todoService.updateTodoStatus(this.todo, true);
  }
  
  deleteTodo(): void {
    this.todoService.deleteTodo(this.todo);
  }
}

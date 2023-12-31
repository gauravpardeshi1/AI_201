import { Component,OnInit  } from '@angular/core';
import { Todo } from '../todo';
import { TodoService } from '../todos';
@Component({
  selector: 'app-todo-list',
  templateUrl: './todo-list.component.html',
  styleUrls: ['./todo-list.component.css']
})
export class TodoListComponent implements OnInit{
  public todos: Todo[] = [];  

  constructor(private todoService: TodoService) { }

  ngOnInit(): void {
    this.todos = this.todoService.getTodos();
  }
}

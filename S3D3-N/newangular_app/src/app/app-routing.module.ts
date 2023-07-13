import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HelloWorldComponent } from './Hello-World/hello-world.component';
import { CounterComponent } from './Counter/counter.component';

const routes: Routes = [
  { path: '', component: HelloWorldComponent },
  { path: 'counter', component: CounterComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

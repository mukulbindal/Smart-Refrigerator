import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { MyrefrigeratorComponent } from './myrefrigerator/myrefrigerator.component';
import { RegisterComponent } from './register/register.component';
import {AuthguardGuard} from './authguard.guard'
const routes: Routes = [
  {path:'register', component:RegisterComponent, canActivate:[AuthguardGuard]},
  {path:'login', component:LoginComponent, canActivate:[AuthguardGuard]},
  {path:'home', component:HomeComponent},
  {path:'myref', component:MyrefrigeratorComponent, canActivate:[AuthguardGuard]},
  {path:'**', redirectTo:'home', pathMatch:'full'},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

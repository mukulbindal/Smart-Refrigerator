import { Component, OnInit, DoCheck } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit, DoCheck {

  constructor(private router : Router) { }
  loggedIn = false;
  ngOnInit(): void {
   if(sessionStorage.getItem('token')){
     this.loggedIn = true;
   }
  }

  ngDoCheck(){
    if(sessionStorage.getItem('token')){
      this.loggedIn = true;
    } else{
      this.loggedIn = false;
    }
  }

  routeTo(comp:string){
    this.router.navigate([comp]);
  }

}

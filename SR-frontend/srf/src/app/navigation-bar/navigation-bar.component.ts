import { Component,DoCheck,OnInit } from '@angular/core';
import { BreakpointObserver, Breakpoints } from '@angular/cdk/layout';
import { Observable } from 'rxjs';
import { map, shareReplay } from 'rxjs/operators';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navigation-bar',
  templateUrl: './navigation-bar.component.html',
  styleUrls: ['./navigation-bar.component.css']
})
export class NavigationBarComponent implements OnInit,DoCheck {
  UID :any = '';
  token :any = '';
  Uname:any = '';
  isHandset$: Observable<boolean> = this.breakpointObserver.observe(Breakpoints.Handset)
    .pipe(
      map(result => result.matches),
      shareReplay()
    );

  constructor(private breakpointObserver: BreakpointObserver, private route:Router) {}
  ngOnInit(){
    this.token = sessionStorage.getItem('token');
    this.Uname = sessionStorage.getItem('Uname');
  }
  
  ngDoCheck(){
    this.token = sessionStorage.getItem('token');
    this.Uname = sessionStorage.getItem('Uname');
  }

  logout(){
    sessionStorage.clear();
    this.route.navigate(['home']);
  }

}

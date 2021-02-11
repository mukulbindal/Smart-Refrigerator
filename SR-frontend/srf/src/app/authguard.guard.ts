import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, UrlTree, Router } from '@angular/router';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthguardGuard implements CanActivate {
  constructor(private route:Router){}
  canActivate(route:ActivatedRouteSnapshot, state:RouterStateSnapshot) {
    if(route.url[0].path === 'login' && sessionStorage.getItem('token')?.length && sessionStorage.getItem('UID')?.length){
      this.route.navigate(['home']);
      return false;
    }
    if(route.url[0].path === 'register' && sessionStorage.getItem('token')?.length && sessionStorage.getItem('UID')?.length){
      this.route.navigate(['home']);
      return false;
    }
    if(route.url[0].path === 'myref' && (!sessionStorage.getItem('token')?.length || !sessionStorage.getItem('UID')?.length))
    {
      this.route.navigate(['home']);
      return false;
    }
    else{
      
    }

    return true;
  }
  
}

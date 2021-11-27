import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class RegisterService {
  url = "http://127.0.0.1:8000/";
  wsURL = "ws://127.0.0.1:8000/"
  constructor(private http:HttpClient) { }

  register(data:any):any{
    let dataString = JSON.stringify(data);
    return this.http.post(this.url+'register',dataString);
  }

  login(data:any):any{
    let dataString = JSON.stringify(data);
    return this.http.post(this.url+'login', dataString);
  }

  detect(data:any):any{
    let dataString = JSON.stringify(data);
    return this.http.get(this.url+'detect');
  }
}

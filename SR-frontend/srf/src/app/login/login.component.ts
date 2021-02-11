import { AfterViewInit, Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { RegisterService } from '../register/register.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit,AfterViewInit {
  loginForm = this.fb.group(
    {
      UID:[null,[Validators.required]],
      password:[null,[Validators.required]]
    }
  )
  constructor(private fb:FormBuilder, private registerService: RegisterService, private router: Router) { }
  UID='';
  token='';
  error='';
  disableSubmit = false;

  @ViewChild('password') passwordButton: ElementRef | any;

  ngAfterViewInit() {
      // console.log(this.myDiv.nativeElement.innerHTML);
  }
 
  ngOnInit(): void {
  }
  reset(){
    this.loginForm.reset();
  }
  onSubmit(){
    this.disableSubmit = true;
    this.loginForm.disable();
    this.error = '';
    this.token = '';
    this.passwordButton.nativeElement.type='password';
    let data = this.loginForm.value;
    this.registerService.login(data).subscribe(
      (res:any)=>{
        console.log(res)
        this.token = res.token;
        this.UID = res.UID;
        sessionStorage.setItem('token',this.token);
        sessionStorage.setItem('UID',this.UID);
        sessionStorage.setItem('Uname',res.Uname);
        sessionStorage.setItem('CamIP',res.CamIP);
        setTimeout(()=>{
          this.router.navigate(['home'])
        },2000);
      },
      (err:any)=>{
        this.loginForm.enable();
        this.disableSubmit = false;
        this.error = err.error.Error || "Something went wrong!";
      }
    )
  }

}

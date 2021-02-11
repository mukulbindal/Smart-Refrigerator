import { Component, ElementRef, ViewChild } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { RegisterService } from './register.service';
@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  registerForm = this.fb.group({
    UNAME: [null, [Validators.required, Validators.pattern(/^[A-z]+(\s[A-z]+)*$/)]],
    password: [null, [Validators.required, Validators.pattern(/^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{6,}$/)]],
    FID: [null, [Validators.required]]
  });

  UID='';
  error=''; 
  disableSubmit = false;

  constructor(private fb: FormBuilder, private registerService:RegisterService) {}
  @ViewChild('password') password:ElementRef|any;
  onSubmit() {
    this.UID='';
    this.error='';
    this.password.nativeElement.type = 'password';
    this.registerForm.disable();
    this.disableSubmit = true;
    this.registerService.register(this.registerForm.value).subscribe(
      (res:any)=>{
        console.log(res)
        this.UID = res.Success.UID;
        this.registerForm.reset();
      },
      (err:any)=>{
        this.error = err.error.Error;
        this.disableSubmit = false;
        this.registerForm.enable();
      }
    )
    
  }
}

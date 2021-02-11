import { Component, DoCheck, OnInit,OnDestroy } from '@angular/core';
import { RegisterService, } from '../register/register.service';

@Component({
  selector: 'app-myrefrigerator',
  templateUrl: './myrefrigerator.component.html',
  styleUrls: ['./myrefrigerator.component.css']
})
export class MyrefrigeratorComponent implements OnInit,DoCheck,OnDestroy {
  listOfItems:any=[];
  emptyRefrigerator = false;
  connectionStatus = "";
  disconnected = false;
  socket:any;
  constructor(private registerService:RegisterService) { }

  ngOnInit(): void {
    // this.loadList();
    this.connectToWeb();
  }
  ngOnDestroy(){
    this.socket.close();
  }
  connectToWeb(){
    const socket = new WebSocket(this.registerService.wsURL+'getref');
    this.socket = socket;
    socket.onopen = (e)=>{
      console.log("Connected", e);
      this.connectionStatus = "Establishing connection to your Refrigerator...";
    }

    socket.onmessage = (e)=>{
      console.log("Message received")
      const data = JSON.parse(e.data);
      if (data === "alive"){
        return;
      }
      else if (data === "CameraError"){
        this.connectionStatus = "Can't reach to Camera at this moment.Please try again later!"
        this.disconnected = true;
        setTimeout(() => {
          socket.close();
        }, 2000);
        return;
      }
      else if(data === "Creating Object"){
        this.connectionStatus = "Connection Established Successfully!";
        setTimeout(() => {
          this.connectionStatus = "Waiting for Smart Vision...";
        }, 2000);
        return;
      } else if(data === "Object Created"){
        this.connectionStatus = "Connected to Smart Vision!";
        socket.send(JSON.stringify({CamIP:sessionStorage.getItem('CamIP')}));
        setTimeout(() => {
          this.connectionStatus = "Analysing your Refrigerator.."
        }, 2000);
        return;
      } else if(data === "empty"){
        this.emptyRefrigerator = true;
        this.listOfItems = [];
        return;
      }
      // console.log(data)
      if(!data.length){
        this.emptyRefrigerator = true;
        return;
      } else {
        this.emptyRefrigerator = false;
      }
      this.listOfItems = [];
      data.forEach((item:any,idx:any) => {
        this.listOfItems.push(
          {
            index:idx,
            name:item.name,
            quantity:item.quantity,
            time:new Date()
          }
        )
      });
    }

    socket.onclose = (e)=>{
      this.connectionStatus = "Disconnected from your Refrigerator. Please refresh the page or try again later."
      this.disconnected = true;
      console.log(e)
    }

  }
  loadList(){
    this.registerService.detect(null).subscribe(
      (res:any)=>{
        console.log(res);
        this.listOfItems= [];
        res.result.forEach((item:any,idx:any) => {
          this.listOfItems.push(
            {
              index:idx,
              name:item.name,
              quantity:1,
              time:0
            }
          )
        });
      },
      (err:any)=>{
        console.log(err)
      }
    )
  }

  ngDoCheck(){
    // this.listOfItems = this.listOfItems;
  }

  

}

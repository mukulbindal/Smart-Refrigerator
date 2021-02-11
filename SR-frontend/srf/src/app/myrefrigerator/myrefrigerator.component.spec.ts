import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MyrefrigeratorComponent } from './myrefrigerator.component';

describe('MyrefrigeratorComponent', () => {
  let component: MyrefrigeratorComponent;
  let fixture: ComponentFixture<MyrefrigeratorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MyrefrigeratorComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(MyrefrigeratorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

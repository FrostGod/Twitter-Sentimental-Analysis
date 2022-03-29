import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { CommonService } from './common.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  form: FormGroup = this.fb.group({
    tagName: [null],
    tweet: [null],
    naiveByes: false,
    baseLine: false,
    decisionTree: false,
    svm: false,
    randomForest: false,
  });
  flag: boolean = true;

  constructor(public commonService: CommonService, private fb: FormBuilder) {}

  ngOnInit(): void {
    this.commonService._get(
      '',
      (res: any) => {
        console.log(res);
      },
      (err: any) => {
        console.log(err);
      }
    );
  }

  saveDetails(form: any) {
    alert('SUCCESS!! :-)\n\n' + JSON.stringify(form.value, null, 4));
  }
}

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
  flag: string = '';

  tweetsResponse: any = [];

  constructor(public commonService: CommonService, private fb: FormBuilder) {}

  ngOnInit(): void {}

  saveDetails(form: any) {
    let queryParams = '';
    if (this.flag === 'tweet') {
      queryParams += 'tweet/' + form.value.tweet;
    } else if (this.flag === 'tag') {
      queryParams += 'topic/' + form.value.tagName;
    }
    queryParams += '?models=';
    if (form.value.naiveByes) {
      queryParams += 'nb,';
    }
    if (form.value.baseLine) {
      queryParams += 'bl,';
    }
    if (form.value.decisionTree) {
      queryParams += 'dt,';
    }
    if (form.value.svm) {
      queryParams += 'svm,';
    }
    if (form.value.randomForest) {
      queryParams += 'rf,';
    }
    queryParams = queryParams.slice(0, -1);
    this.commonService._get(
      queryParams,
      (res: any) => {
        let idx = 0;
        console.log(res);
        while (res[idx] !== undefined) {
          this.tweetsResponse.push(res[idx]);
          idx++;
        }
      },
      (err: any) => {
        console.log(err);
      }
    );
  }
}

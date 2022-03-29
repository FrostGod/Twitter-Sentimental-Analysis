import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root',
})
export class CommonService {
  constructor(private http: HttpClient, public router: Router) {}

  _get(apiUrl: any, success: any, failure: any) {
    this.http.get(`https://www.google.co.in/`).subscribe(
      (res) => {
        success(res);
      },
      (err) => {
        failure(err);
      }
    );
  }
}

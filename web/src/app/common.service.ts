import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { environment } from '../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class CommonService {
  constructor(private http: HttpClient, public router: Router) {}

  _get(apiUrl: any, success: any, failure: any) {
    this.http.get(`${environment.serverUrl}${apiUrl}`).subscribe(
      (res) => {
        success(res);
      },
      (err) => {
        failure(err);
      }
    );
  }
}

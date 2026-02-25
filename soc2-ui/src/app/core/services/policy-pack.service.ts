import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../environments/environment';

@Injectable({ providedIn: 'root' })
export class PolicyPackService {
  constructor(private http: HttpClient) {}

  generatePack() {
    // responseType: 'blob' is required for ZIP download
    return this.http.post(`${environment.apiBaseUrl}/api/policy-pack/generate`, {}, { responseType: 'blob' });
  }
}

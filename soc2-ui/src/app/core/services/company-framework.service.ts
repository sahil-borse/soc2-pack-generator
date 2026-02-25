import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../environments/environment';

export interface CompanyFramework {
  frameworkId: string;
  name: string;
  version: string;
  enabledAt: string;
  score: number;
}

@Injectable({
  providedIn: 'root',
})
export class CompanyFrameworkService {

  constructor(private http: HttpClient) {}

  getCompanyFrameworks() {
    return this.http.get<CompanyFramework[]>(`${environment.apiBaseUrl}/api/company-frameworks`);
  }

  enableFramework(frameworkId: string) {
    return this.http.post(
      `${environment.apiBaseUrl}/api/company-frameworks`,
      { frameworkId }
    );
  }
}
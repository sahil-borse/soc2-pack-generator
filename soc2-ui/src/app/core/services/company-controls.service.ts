import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';

export interface CompanyControl {
  id: string;
  controlCode: string;
  title: string;
  category?: string;
  status: string;
}

@Injectable({
  providedIn: 'root'
})
export class CompanyControlsService {

  constructor(private http: HttpClient) {}

  getControls(frameworkId: string): Observable<CompanyControl[]> {
    return this.http.get<CompanyControl[]>(
      `${environment.apiBaseUrl}/api/company-controls?frameworkId=${frameworkId}`
    );
  }

  updateStatus(controlId: string, status: string) {
    return this.http.patch(`${environment.apiBaseUrl}/api/company-controls/${controlId}`, { status });
  }
}
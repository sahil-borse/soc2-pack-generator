import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../environments/environment';
import { Observable } from 'rxjs';

export interface CompanyProfileApiResponse {
  id: string;
  userId: string;
  profile: any;
  createdAt?: string;
  updatedAt?: string;
}

@Injectable({ providedIn: 'root' })
export class CompanyProfileService {
  constructor(private http: HttpClient) {}

  getProfile(): Observable<CompanyProfileApiResponse> {
    return this.http.get<CompanyProfileApiResponse>(`${environment.apiBaseUrl}/api/company-profile`);
  }

  saveProfile(profile: any): Observable<{ ok: boolean }> {
    return this.http.put<{ ok: boolean }>(`${environment.apiBaseUrl}/api/company-profile`, {
      profile,
    });
  }
}

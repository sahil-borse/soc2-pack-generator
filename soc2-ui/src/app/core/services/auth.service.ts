import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../environments/environment';
import { tap } from 'rxjs/operators';
import { Observable } from 'rxjs';

export interface AuthResponse {
  accessToken: string;
  user: {
    id: string;
    email: string;
    createdAt: string;
  };
}

@Injectable({ providedIn: 'root' })
export class AuthService {
  private readonly tokenKey = 'soc2_token';

  constructor(private http: HttpClient) {}

  register(email: string, password: string): Observable<AuthResponse> {
    return this.http
      .post<AuthResponse>(`${environment.apiBaseUrl}/api/auth/register`, { email, password })
      .pipe(tap((res) => this.setToken(res.accessToken)));
  }

  login(email: string, password: string): Observable<AuthResponse> {
    return this.http
      .post<AuthResponse>(`${environment.apiBaseUrl}/api/auth/login`, { email, password })
      .pipe(tap((res) => this.setToken(res.accessToken)));
  }

  logout(): void {
    localStorage.removeItem(this.tokenKey);
  }

  setToken(token: string): void {
    localStorage.setItem(this.tokenKey, token);
  }

  getToken(): string | null {
    return localStorage.getItem(this.tokenKey);
  }

  isLoggedIn(): boolean {
    return !!this.getToken();
  }
}

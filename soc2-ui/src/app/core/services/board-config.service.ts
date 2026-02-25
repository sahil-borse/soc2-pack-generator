import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';

export interface BoardColumn {
  key: string;
  label: string;
  order: number;
}

@Injectable({
  providedIn: 'root'
})
export class BoardConfigService {

  constructor(private http: HttpClient) {}

  getConfig(frameworkId: string): Observable<{ columns: BoardColumn[] }> {
    return this.http.get<{ columns: BoardColumn[] }>(
      `${environment.apiBaseUrl}/api/board-config?frameworkId=${frameworkId}`
    );
  }

  updateConfig(frameworkId: string, columns: BoardColumn[]) {
    return this.http.post(`${environment.apiBaseUrl}/api/board-config`, {
      frameworkId,
      columns
    });
  }
}
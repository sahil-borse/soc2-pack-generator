import { Routes } from '@angular/router';
import { authGuard } from './core/guards/auth-guard';

import { LoginComponent } from './pages/login/login';
import { RegisterComponent } from './pages/register/register';
import { DashboardComponent } from './pages/dashboard/dashboard';
import { CompanyProfileComponent } from './pages/company-profile/company-profile';
import { DocumentsComponent } from './pages/documents/documents';


export const routes: Routes = [
  { path: '', pathMatch: 'full', redirectTo: 'dashboard' },

  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },

  { path: 'dashboard', component: DashboardComponent, canActivate: [authGuard] },
  { path: 'company-profile', component: CompanyProfileComponent, canActivate: [authGuard] },
  { path: 'documents', component: DocumentsComponent, canActivate: [authGuard] },

  { path: '**', redirectTo: 'dashboard' },

];

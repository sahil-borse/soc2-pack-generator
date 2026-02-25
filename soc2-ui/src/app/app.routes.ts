import { Routes } from '@angular/router';
import { authGuard } from './core/guards/auth-guard';

import { LoginComponent } from './pages/login/login';
import { RegisterComponent } from './pages/register/register';
import { DashboardComponent } from './pages/dashboard/dashboard';
import { CompanyProfileComponent } from './pages/company-profile/company-profile';
import { DocumentsComponent } from './pages/documents/documents';
import { companyGuard } from './core/guards/company.guard';
import { CreateCompanyComponent } from './pages/create-company/create-company';
import { ControlsComponent } from './pages/controls/controls'


export const routes: Routes = [
  { path: '', pathMatch: 'full', redirectTo: 'dashboard' },

  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },

  { path: 'dashboard', component: DashboardComponent, canActivate: [authGuard, companyGuard] },
  { path: 'company-profile', component: CompanyProfileComponent, canActivate: [authGuard, companyGuard] },
  { path: 'documents', component: DocumentsComponent, canActivate: [authGuard, companyGuard] },
  { path: 'create-company', component: CreateCompanyComponent, canActivate: [authGuard] },
  { path: 'controls/:frameworkId', component: ControlsComponent,  canActivate: [authGuard]},

  { path: '**', redirectTo: 'dashboard' },

];

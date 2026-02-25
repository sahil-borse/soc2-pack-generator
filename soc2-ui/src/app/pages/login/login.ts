import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { Router, RouterModule } from '@angular/router';
import { AuthService } from '../../core/services/auth.service';
import { CompanyService } from '../../core/services/company.service'

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, RouterModule],
  templateUrl: './login.html',
  styleUrl: './login.css',
})
export class LoginComponent {
  loading = false;
  error = '';
  form: FormGroup;

  constructor(
    private fb: FormBuilder,
    private auth: AuthService,
    private companyService: CompanyService,
    private router: Router
  ) {
    this.form = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(8)]],
    });
  }

  submit() {
    this.error = '';

    if (this.form.value.email.invalid) {
      this.error = 'Please enter valid email.';
      return;
    }
    if (this.form.value.password.invalid) {
      this.error = 'Please enter valid password.';
      return;
    }

    this.loading = true;

    const email = this.form.value.email;
    const password = this.form.value.password;

    this.auth.login(email, password).subscribe({
      next: () => {
        this.loading = false;
        this.router.navigate(['/dashboard']);

        this.companyService.getCompanies().subscribe({
          next: (companies) => {
            if (companies.length === 1) {
              localStorage.setItem('companyId', companies[0].id);
              this.router.navigate(['/dashboard']);
            } else if (companies.length === 0) {
              this.router.navigate(['/create-company']);
            } else {
              this.router.navigate(['/select-company']);
            }
          }
        });
      },
      error: (err) => {
        this.loading = false;
        this.error = err?.error?.detail || 'Login failed';
      },
    });
  }
}

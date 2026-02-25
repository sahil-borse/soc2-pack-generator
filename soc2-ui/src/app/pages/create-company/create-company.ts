import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, ReactiveFormsModule, Validators, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';
import { CompanyService } from '../../core/services/company.service';

@Component({
  selector: 'app-create-company',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './create-company.html'
})
export class CreateCompanyComponent {

  form!: FormGroup;
  loading = false;
  error = '';

  constructor(
    private fb: FormBuilder,
    private companyService: CompanyService,
    private router: Router
  ) {
    // ✅ Initialize form HERE
    this.form = this.fb.group({
      name: ['', Validators.required]
    });
  }

  submit() {
  if (this.form.invalid) return;

  this.loading = true;

  this.companyService.createCompany(this.form.value).subscribe({
    next: (res: any) => {
      console.log("company: ", res.id)
      localStorage.setItem('companyId', res.id);
      this.router.navigate(['/dashboard']);
    },
    error: () => {
      this.loading = false;
      this.error = 'Failed to create company';
    }
  });
}
}
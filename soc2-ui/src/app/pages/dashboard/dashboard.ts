import { Component, OnInit, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { CompanyFrameworkService, CompanyFramework } from '../../core/services/company-framework.service';
@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './dashboard.html'
})
export class DashboardComponent implements OnInit {

  frameworks = signal<CompanyFramework[]>([]);
  loading = signal(true);  

  constructor(private service: CompanyFrameworkService) { }

  ngOnInit() {
    this.service.getCompanyFrameworks().subscribe({
      next: (res) => {
        this.frameworks.set(res);
      },
      error: () => {
        console.error('Failed to load frameworks');
      }
    });
    this.loading.set(false);
  }

  progressColor(score: number) {
    if (score >= 80) return 'bg-green-500';
    if (score >= 50) return 'bg-yellow-500';
    return 'bg-red-500';
  }
  
}
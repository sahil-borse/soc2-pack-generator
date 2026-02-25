import { Component, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { PolicyPackService } from '../../core/services/policy-pack.service';

@Component({
  selector: 'app-documents',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './documents.html',
  styleUrl: './documents.css',
})
export class DocumentsComponent {
  generating = signal(false);
  error = signal('');
  message = signal('');

  constructor(private policyPack: PolicyPackService) {}

  generateAndDownload() {
    this.error.set('');
    this.message.set('');
    this.generating.set(true);

    this.policyPack.generatePack().subscribe({
      next: (blob) => {
        this.generating.set(false);
        this.message.set('Policy pack generated ✅ Download started.');

        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'soc2_policy_pack.zip';
        a.click();
        window.URL.revokeObjectURL(url);
      },
      error: (err) => {
        console.error(err);
        this.generating.set(false);
        this.error.set(err?.error?.detail || 'Failed to generate policy pack');
      },
    });
  }
}

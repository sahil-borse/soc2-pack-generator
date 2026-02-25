import { Component, OnInit, signal  } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { CompanyProfileService } from '../../core/services/company-profile.service';

@Component({
  selector: 'app-company-profile',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, RouterModule],
  templateUrl: './company-profile.html',
  styleUrl: './company-profile.css',
})
export class CompanyProfileComponent implements OnInit{
  loading = signal(true);
  saving = false;
  message = '';
  error = '';

  form: FormGroup;

  constructor(
    private fb: FormBuilder,
    private service: CompanyProfileService
  ) {
    this.form = this.fb.group({
      legalName: ['', [Validators.required]],
      industry: ['SaaS', [Validators.required]],
      headcount: [10, [Validators.required, Validators.min(1)]],
      remoteWork: ['Hybrid', [Validators.required]],

      cloudProvider: ['AWS'],
      sourceControl: ['GitHub'],
      ciCd: ['GitHub Actions'],
      ticketingTool: ['Jira'],
      documentationTool: ['Confluence'],
      chatTool: ['Slack'],

      ssoUsed: [true],
      ssoProvider: ['Google Workspace'],
      mfaEnforcedForAllUsers: [true],
      accessReviewFrequency: ['Quarterly'],
      offboardingTimelineHours: [24],
    });
  }

  ngOnInit() {

    this.load();
  }

  load() {
  this.loading.set(true);

  this.error = '';
  this.message = '';

  this.service.getProfile().subscribe({
    next: (res) => {
      const p = (res as any)?.profile || {};
      console.log('PROFILE:', p);

      try {
        this.form.patchValue({
          legalName: p?.company?.legalName || '',
          industry: p?.company?.industry || 'SaaS',
          headcount: p?.company?.headcount || 10,
          remoteWork: p?.company?.remoteWork || 'Hybrid',

          cloudProvider: p?.itEnvironment?.cloudProvider || 'AWS',
          sourceControl: p?.itEnvironment?.sourceControl || 'GitHub',
          ciCd: p?.itEnvironment?.ciCd || 'GitHub Actions',
          ticketingTool: p?.itEnvironment?.ticketingTool || 'Jira',
          documentationTool: p?.itEnvironment?.documentationTool || 'Confluence',
          chatTool: p?.itEnvironment?.chatTool || 'Slack',

          ssoUsed: p?.identityAndAccess?.ssoUsed ?? true,
          ssoProvider: p?.identityAndAccess?.ssoProvider || 'Google Workspace',
          mfaEnforcedForAllUsers: p?.identityAndAccess?.mfaEnforcedForAllUsers ?? true,
          accessReviewFrequency: p?.identityAndAccess?.accessReviewFrequency || 'Quarterly',
          offboardingTimelineHours: p?.identityAndAccess?.offboardingTimelineHours || 24,
        });
      } catch (e) {
        console.error('PATCH ERROR:', e);
      }

      this.loading.set(false);
    },

    error: (err) => {
      console.error(err);
      this.loading.set(false);
      this.error = 'Failed to load company profile';
    },
  });
}


  save() {
    this.saving = true;
    this.error = '';
    this.message = '';

    const v = this.form.value;

    const profile = {
      company: {
        legalName: v.legalName,
        industry: v.industry,
        headcount: Number(v.headcount),
        remoteWork: v.remoteWork,
        locations: ['India'],
      },
      itEnvironment: {
        cloudProvider: v.cloudProvider,
        sourceControl: v.sourceControl,
        ciCd: v.ciCd,
        ticketingTool: v.ticketingTool,
        documentationTool: v.documentationTool,
        chatTool: v.chatTool,
      },
      identityAndAccess: {
        ssoUsed: !!v.ssoUsed,
        ssoProvider: v.ssoProvider,
        mfaEnforcedForAllUsers: !!v.mfaEnforcedForAllUsers,
        accessReviewFrequency: v.accessReviewFrequency,
        offboardingTimelineHours: Number(v.offboardingTimelineHours),
      },
    };

    this.service.saveProfile(profile).subscribe({
      next: () => {
        this.saving = false;
        this.message = 'Saved successfully ✅';
      },
      error: (err) => {
        this.saving = false;
        this.error = err?.error?.detail || 'Save failed';
      },
    });
  }
}

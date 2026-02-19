import { TestBed } from '@angular/core/testing';

import { CompanyProfile } from './company-profile';

describe('CompanyProfile', () => {
  let service: CompanyProfile;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CompanyProfile);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});

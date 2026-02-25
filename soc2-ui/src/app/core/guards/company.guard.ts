import { CanActivateFn } from '@angular/router';
import { inject } from '@angular/core';
import { Router } from '@angular/router';

export const companyGuard: CanActivateFn = () => {
  const companyId = localStorage.getItem('companyId');

  if (!companyId) {
    return inject(Router).createUrlTree(['/create-company']);
  }

  return true;
};
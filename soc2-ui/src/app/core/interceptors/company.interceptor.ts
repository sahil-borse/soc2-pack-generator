import { HttpInterceptorFn } from '@angular/common/http';

export const companyInterceptor: HttpInterceptorFn = (req, next) => {
  const companyId = localStorage.getItem('companyId');

  if (!companyId) {
    return next(req);
  }

  const cloned = req.clone({
    setHeaders: {
      'X-Company-Id': companyId
    }
  });

  return next(cloned);
};
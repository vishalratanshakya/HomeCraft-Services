"use client";

import { useEffect } from 'react';
import { useRouter } from 'next/navigation';

export default function AdminBannersRedirectPage() {
  const router = useRouter();
  useEffect(() => {
    router.replace('/admin/dashboard?tab=banners');
  }, [router]);

  return null;
}

Name:           perl-Test-Memory-Cycle
Version:        1.04
Release:        7.1%{?dist}
Summary:        Check for memory leaks and circular memory references

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Test-Memory-Cycle/
Source0:        http://www.cpan.org/authors/id/P/PE/PETDANCE/Test-Memory-Cycle-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(Devel::Cycle) >= 1.07
BuildRequires:  perl(PadWalker)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::Simple) >= 0.62
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Perl's garbage collection has one big problem: Circular references
can't get cleaned up.  A circular reference can be as simple as two
objects that refer to each other.
"Test::Memory::Cycle" is built on top of "Devel::Cycle" to give you an
easy way to check for these circular references.


%prep
%setup -q -n Test-Memory-Cycle-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/Test/
%{_mandir}/man3/*.3pm*


%changelog
* Mon Apr 26 2010 Dennis Gregorovic <dgregor@redhat.com> - 1.04-7.1
- Rebuilt for RHEL 6
Related: rhbz#566527

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.04-5
- Rebuild normally, second pass

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.04-4
- Rebuild for perl 5.10 (again), first pass

* Mon Jan 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.04-3
- rebuild normally, second pass

* Sun Jan 13 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.04-2
- rebuild for new perl, disable T-P-C and tests for first pass

* Wed Aug  9 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.04-1
- Update to 1.04.

* Mon Feb 20 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.02-2
- Rebuild for FC5 (perl 5.8.8).

* Tue May 24 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.02-1
- Update to 1.02.

* Sat May 14 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.00-4
- Add dist tag.

* Fri Apr 22 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.00-3
- Fedora Extras: FC-4 version.

* Fri Apr 22 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.00-2
- Fedora Extras: FC-3 version.

* Wed Apr 20 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.00-0.fdr.2
- RedHat 9.0 (8.0 and 7.3): CGI.pm is shipped as perl-CGI (#1824).

* Mon Jan 24 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.00-0.fdr.1
- Update to 1.00.

* Sun Jul 04 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:0.02-0.fdr.1
- First build.

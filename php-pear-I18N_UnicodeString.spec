%include	/usr/lib/rpm/macros.php
%define		_class		I18N
%define		_subclass	UnicodeString
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - provides a way to work with self contained multibyte strings
Summary(pl):	%{_pearname} - sposób pracy z samodzielnymi ³añcuchami znaków wielobajtowych
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	251d67d3463af5768ece323b6c7c4336
URL:		http://pear.php.net/package/I18N_UnicodeString/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a method of storing and manipulating multibyte strings in PHP
without using ext/mbstring. Also allows conversion between various
methods of storing Unicode in 1-byte strings like UTF-8 and HTML
entities.

In PEAR status of this package is: %{_status}.

%description -l pl
Ta klasa dostarcza metodê zapisu i obróbki ³añcuchów znaków
wielobajtowych w PHP bez u¿ywania rozszerzenia mbstring. Umo¿liwia
tak¿e konwersjê miêdzy ró¿nymi metodami zapisu Unikodu w ³añcuchach
znaków jednobajtowych, takich jak UTF-8 czy encje HTML.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/examples
%{php_pear_dir}/%{_class}/*.php

%define		cvs_release	20030906
%define		orig_name	cairo-gtk-engine
Summary:	Cairo graphics engine for GTK+
Summary(pl):	Silnik graficzny Cairo dla GTK+
Name:		gtk2-theme-engine-Cairo
Version:	0.4
Release:	0.%{cvs_release}.4
# uhm... whole cairo is on BSD-like, but this package contains only
# COPYING file with GPL and no other license notes
License:	GPL (?)
Group:		Themes/GTK+
Source0:	%{orig_name}-cvs-%{cvs_release}.tar.gz
Patch0:		%{orig_name}-pixpath.patch
# Source0-md5:	f2d33ec1b0af8c49ee0d0f2c682e250b
URL:		http://gtk-themes.cairographics.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	cairo-devel >= 0.1.1
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.9.0
Requires:	gnome-themes-extras
Provides:	cairo-gtk-engine
Obsoletes:	cairo-gtk-engine
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains Cairo test GTK+ engine.

%description -l pl
Ten pakiet zawiera testowy silnik graficzny Cairo dla GTK+.

%prep
%setup -q -n %{orig_name}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no *.la for gtk engines
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/*/engines/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/gtk-2.0/*/engines/*.so
%{_datadir}/themes/*

%include	/usr/lib/rpm/macros.perl
Summary:	Frozen Bubble arcade game
Summary(pl):	Gra zr�czno�ciowa Frozen Bubble
Name:		frozen-bubble
Version:	1.0.0
Release:	5
License:	GPL
Group:		X11/Applications/Games
Source0:	http://people.mandrakesoft.com/~gc/fb/%{name}-%{version}.tar.bz2
# Source0-md5:	2be5ead2aee72adc3fb643630a774b59
Source1:	%{name}.desktop
#Icon:		%{name}.xpm
URL:		http://www.frozen-bubble.org/
BuildRequires:	SDL_mixer-devel >= 1.2.2
BuildRequires:	perl-SDL >= 1.19
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	smpeg-devel
Requires:	perl-SDL >= 1.19
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(fbmdkcommon)' 'perl(Gimp)'

%description
Full-featured, colorful animated penguin eyecandy, 50 levels of 1p
game, hours and hours of 2p game, 3 professional quality 20-channels
musics, 15 stereo sound effects, 7 unique graphical transition
effects.

%description -l pl
Gra o wielu mo�liwo�ciach, z kolorowymi animacjami, 50-ma poziomami
dla jednego gracza, wieloma godzinami zabawy dla dw�ch graczy, 3-ma
profesjonalnej jako�ci 20-kana�owymi muzyczkami, 15-ma
stereofonicznymi efektami d�wi�kowymi, 7-ma unikalnymi graficznymi
efektami przej��.

%prep
%setup -q

%build
%{__make} \
	OPTIMIZE="%{rpmcflags} -Wall" \
	PREFIX="%{_prefix}" \
	INSTALLDIRS=vendor

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir},%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT/usr \
	DESTDIR=$RPM_BUILD_ROOT

install icons/%{name}-icon-48x48.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/gfx/.xvpics

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS CHANGES
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%dir %{perl_vendorarch}/auto/fb_c_stuff
%{perl_vendorarch}/auto/fb_c_stuff/fb_c_stuff.bs
%attr(755,root,root) %{perl_vendorarch}/auto/fb_c_stuff/fb_c_stuff.so
%{perl_vendorarch}/*.pm
%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop
%{_mandir}/man6/*

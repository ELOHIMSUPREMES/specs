%set_verify_elf_method unresolved=strict

Name: gnustep-themes-Narcissus
Version: r6046
Release: alt1.svn20100419
Summary: GNUstep's Narcissus theme
License: Free
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/etoile/mockups/narcissus/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gnustep/gnustep-easydiff.git
Source: %name-%version.tar

%description
Narcissus theme for GNUstep.

%prep
%setup

%install
install -d %buildroot%_libdir/GNUstep/Themes/Narcissus.theme
cp -fR Resources %buildroot%_libdir/GNUstep/Themes/Narcissus.theme/

%files
%_libdir/GNUstep

%changelog
* Tue Feb 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r6046-alt1.svn20100419
- Initial build for Sisyphus


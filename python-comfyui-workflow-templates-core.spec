Name:		python-comfyui-workflow-templates-core
Version:	0.3.396
Release:	1
Summary:	Loader for ComfyUI workflow templates
License:	MIT
Group:		Development/Python
URL:		https://github.com/Comfy-Org/workflow_templates
Source0:	https://files.pythonhosted.org/packages/source/c/comfyui-workflow-templates-core/comfyui_workflow_templates_core-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)

%description
Manifest and loader used by the ComfyUI workflow template
bundles.

%files
%{py_sitedir}/comfyui_workflow_templates_core
%{py_sitedir}/comfyui_workflow_templates_core-*.*-info

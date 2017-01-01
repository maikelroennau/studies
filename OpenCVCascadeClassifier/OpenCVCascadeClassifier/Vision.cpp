#include "Vision.h"

using namespace System;
using namespace System::Windows::Forms;

[STAThread]
void main(array<String^>^ argv)
{
	Application::EnableVisualStyles();
	Application::SetCompatibleTextRenderingDefault(false);

	OpenCVCascadeClassifier::Vision mainForm;
	Application::Run(%mainForm);
}
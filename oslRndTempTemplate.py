import pymel.core as pm
from mtoa.ui.ae.shaderTemplate import ShaderAETemplate
 
class AEoslRndTempTemplate(ShaderAETemplate):
 
    def setup(self):
        # Add the shader swatch to the AE
        self.addSwatch()
        self.beginScrollLayout()
 
        # Add a list that allows to replace the shader for other one
        self.addCustom('message', 'AEshaderTypeNew',
        'AEshaderTypeReplace')
 
        # Begins a "Color Section"
        self.beginLayout("Color Section", collapse=False)
        self.addControl('floatA', label='floatParamA', annotation='Constant floatA')
		self.addControl('floatB', label='floatParamB', annotation='Constant floatB')
		#self.addControl('colorB', label='ColorB', annotation='Constant ColorB')
		self.endLayout()
		
        # include/call base class/node attributes
        pm.mel.AEdependNodeTemplate(self.nodeName)
 
        # Add Section for the extra controls not displayed before
        self.addExtraControls()
        self.endScrollLayout()
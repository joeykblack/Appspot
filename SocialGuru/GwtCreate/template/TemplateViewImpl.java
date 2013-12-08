package project.gwt.package.client.view.impl;

import com.google.gwt.user.client.ui.Composite;
import com.google.gwt.uibinder.client.UiBinder;
import com.google.gwt.user.client.ui.Widget;
import com.google.gwt.core.client.GWT;

import project.gwt.package.client.view.TemplateView;

/**
 * @author joeykblack
 *
 */
public class TemplateViewImpl extends Composite implements TemplateView
{

	private static TemplateViewImplUiBinder uiBinder = GWT.create(TemplateViewImplUiBinder.class);
	interface TemplateViewImplUiBinder extends UiBinder<Widget, TemplateViewImpl> {}
	
	
	public TemplateViewImpl() 
	{
		initWidget(uiBinder.createAndBindUi(this));
	}

}

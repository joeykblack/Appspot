package project.gwt.package.client.gin;

import project.gwt.package.client.view.TemplateView;
import project.gwt.package.client.activity.impl.TemplateActivityImpl;

import com.google.gwt.event.shared.EventBus;
import com.google.gwt.inject.client.GinModules;
import com.google.gwt.inject.client.Ginjector;


/**
 * @author joeykblack
 *
 */
@GinModules(TemplateGinModule.class)
public interface TemplateGinjector extends Ginjector
{
	
	TemplateView getTemplateView();
	EventBus getEventBus();
	TemplateActivityImpl getTemplateActivityImpl();
	
}
package project.gwt.package.client.gin;

import project.gwt.package.client.view.TemplateView;
import project.gwt.package.client.view.impl.TemplateViewImpl;
import project.gwt.package.client.activity.impl.TemplateActivityImpl;
import project.gwt.package.client.activity.TemplateActivity;

import com.google.gwt.event.shared.EventBus;
import com.google.gwt.event.shared.SimpleEventBus;
import com.google.gwt.inject.client.AbstractGinModule;
import com.google.inject.Singleton;


/**
 * @author joeykblack
 *
 */
public class TemplateGinModule extends AbstractGinModule
{
	
	@Override
	protected void configure()
	{
		bind(TemplateView.class).to(TemplateViewImpl.class).in(Singleton.class);
		bind(EventBus.class).to(SimpleEventBus.class).in(Singleton.class);
		bind(TemplateActivity.class).to(TemplateActivityImpl.class);
	}
	
}
/**
 * 
 */
package project.gwt.package.client.factory.impl;

import com.google.gwt.event.shared.EventBus;
import com.google.gwt.event.shared.SimpleEventBus;
import com.google.gwt.place.shared.PlaceController;

import project.gwt.package.client.view.impl.TemplateViewImpl;
import project.gwt.package.client.view.TemplateView;

import project.gwt.package.client.factory.ClientFactory;

/**
 * @author joey
 *
 */
public class ClientFactoryImpl implements ClientFactory
{
	private static final TemplateViewImpl templateViewImpl = new TemplateViewImpl();
	private static final EventBus eventBus = new SimpleEventBus();
	private static final PlaceController placeController = new PlaceController(eventBus);
	
	public TemplateView getTemplateView()
	{
		return templateViewImpl;
	}

	public EventBus getEventbus()
	{
		return eventBus;
	}

	public PlaceController getPlacecontroller()
	{
		return placeController;
	}
	

}

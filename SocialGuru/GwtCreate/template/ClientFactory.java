/**
 * 
 */
package project.gwt.package.client.factory;

import com.google.gwt.event.shared.EventBus;
import com.google.gwt.place.shared.PlaceController;

import project.gwt.package.client.view.TemplateView;

/**
 * @author joey
 *
 */
public interface ClientFactory 
{
	
	public TemplateView getTemplateView();

	public EventBus getEventbus();

	public PlaceController getPlacecontroller();

}

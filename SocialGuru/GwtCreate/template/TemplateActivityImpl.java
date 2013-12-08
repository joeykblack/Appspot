/**
 * 
 */
package project.gwt.package.client.activity.impl;

import project.gwt.package.client.Template;
import project.gwt.package.client.activity.TemplateActivity;
import project.gwt.package.client.view.TemplateView;

import com.google.gwt.activity.shared.AbstractActivity;
import com.google.gwt.event.shared.EventBus;
import com.google.gwt.place.shared.Place;
import com.google.gwt.user.client.ui.AcceptsOneWidget;

/**
 * @author joeykblack
 *
 */
public class TemplateActivityImpl extends AbstractActivity implements TemplateActivity
{

	@Override
	public void start(AcceptsOneWidget containerWidget, EventBus eventBus)
	{
		TemplateView templateView = Template.factory.getTemplateView();
		containerWidget.setWidget(templateView.asWidget());
		
	}

	@Override
	public void goTo(Place place)
	{
		Template.factory.getPlacecontroller().goTo(place);
	}

}
